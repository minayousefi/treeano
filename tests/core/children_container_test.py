import nose.tools as nt
from treeano import core
import treeano


def test_list_children_container():
    # test to_data
    cc = core.ListChildrenContainer([])
    nt.assert_equal([], cc.to_data())

    # test children_container_to_data
    as_data = core.children_container_to_data(cc)
    nt.assert_equal(dict(
        children_container_key="list",
        children_container_data=[],
    ),
        as_data)

    # test back and forth
    cc2 = core.children_container_from_data(as_data)
    nt.assert_is_instance(cc2, core.ListChildrenContainer)
    nt.assert_equal(as_data,
                    core.children_container_to_data(cc2))


def test_dict_children_container():
    # test to_data
    cc = core.DictChildrenContainer({})
    nt.assert_equal({}, cc.to_data())

    # test children_container_to_data
    as_data = core.children_container_to_data(cc)
    nt.assert_equal(dict(
        children_container_key="dict",
        children_container_data={},
    ),
        as_data)

    # test back and forth
    cc2 = core.children_container_from_data(as_data)
    nt.assert_is_instance(cc2, core.DictChildrenContainer)
    nt.assert_equal(as_data,
                    core.children_container_to_data(cc2))


def test_dict_children_container_schema():
    dccs = core.DictChildrenContainerSchema(
        foo=core.ListChildrenContainer,
        bar=core.ChildContainer,
    )
    node = treeano.nodes.toy.AddConstantNode("hello")
    cc1 = dccs({"foo": [node, node], "bar": node})
    cc2 = core.DictChildrenContainer(
        {"foo": core.ListChildrenContainer([node, node]),
         "bar": core.ChildContainer(node)})
    nt.assert_equal(cc1, cc2)
