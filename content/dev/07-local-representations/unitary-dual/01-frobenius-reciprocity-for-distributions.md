---
title: Frobenius reciprocity for equivariant distributions
decls:
  - PositivityTheory.PfBern.Frob.frobeniusReciprocity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frobenius reciprocity for equivariant distributions

Let $G$ be a totally disconnected group that acts on a space $X$ fibred over $G/H$. A distribution on $X$ that transforms under $G$ by a character is fixed by its restriction to the fibre over the base point, and this restriction is an $H$-equivariant distribution on the fibre. This is Frobenius reciprocity for distributions, in the form of Bernstein and Zelevinsky. This section proves it with an explicit formula and with control of supports. The vanishing theorems of the next two sections use it to move from a fibre bundle to a smaller group, and the step [EveryCharacter](/step/every-character/) uses it through them.

Background: [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [[Haar measure|VY0HXD3GC4]].

### Distributions on totally disconnected spaces

A topological space is an *$l$-space* if it is Hausdorff, locally compact and totally disconnected. For an $l$-space $X$, let $S(X)$ be the space of locally constant, compactly supported functions $X \to \mathbb{C}$. A *distribution* on $X$ is a linear functional $\xi : S(X) \to \mathbb{C}$, with no continuity condition.

Let $C \subseteq X$ be closed. A distribution $\xi$ is *supported in $C$* if $\xi(f) = 0$ for every $f \in S(X)$ whose support lies in $X \setminus C$.

Let a group $G$ act continuously on $X$. For $g \in G$ and $f \in S(X)$ put $(g \cdot f)(x) = f(g^{-1}x)$.

Let $\chi : G \to \mathbb{C}^\times$ be a continuous character. A distribution $\xi$ on $X$ is *$\chi$-equivariant* if $\xi(g \cdot f) = \chi(g)\,\xi(f)$ for all $g \in G$ and $f \in S(X)$.

### The theorem

Fix the following data.

- $G$ is a second countable $l$-group with its Borel structure, and $H \leq G$ is a closed subgroup. Both $G$ and $H$ are unimodular. Let $\mu_G$ and $\mu_H$ be Haar measures.
- $X$ is an $l$-space with a continuous action of $G$, and $p : X \to G/H$ is a continuous $G$-equivariant map.
- $F = p^{-1}(1 \cdot H)$ is the fibre over the base point. It is closed in $X$ and stable under $H$.
- $\chi : G \to \mathbb{C}^\times$ is a continuous character.

Let $\mathcal{D}(X)^{G,\chi}$ be the space of $\chi$-equivariant distributions on $X$, and $\mathcal{D}(F)^{H,\chi}$ the space of $\chi|_H$-equivariant distributions on $F$.

**Theorem 7.1.1 (Frobenius reciprocity).** There is a linear isomorphism
$$\mathrm{Fr} : \mathcal{D}(X)^{G,\chi} \to \mathcal{D}(F)^{H,\chi}$$
with the following two properties.

1. Let $C \subseteq X$ be closed and $G$-stable. Then $\xi$ is supported in $C$ if and only if $\mathrm{Fr}(\xi)$ is supported in $F \cap C$.
2. Let $\alpha \in S(G)$, $\varphi \in S(F)$ and $f \in S(X)$ satisfy
$$f(g z) = \int_H \alpha(g h)\, \varphi(h^{-1} z)\, d\mu_H(h) \quad \text{for all } g \in G,\ z \in F.$$
Then
$$\xi(f) = \Big( \int_G \alpha\, \chi \, d\mu_G \Big) \cdot \mathrm{Fr}(\xi)(\varphi).$$

Lean: `PositivityTheory.PfBern.Frob.frobeniusReciprocity`.

The formula in 2 fixes $\mathrm{Fr}(\xi)$: for each $\varphi$, choose $\alpha$ with $\int_G \alpha \chi \neq 0$, and the right side gives $\mathrm{Fr}(\xi)(\varphi)$.

*Proof.* The proof follows Bernstein and Zelevinsky. It has four steps.

*Step 1: the bundle.* Let $H$ act on $G \times F$ by $h \cdot (g, z) = (g h^{-1}, h z)$. The map $(g, z) \mapsto g z$ is constant on $H$-orbits and gives a continuous bijection $G \times^H F \to X$. Indeed, if $p(x) = gH$ then $g^{-1} x \in F$, and $g z = g' z'$ with $z, z' \in F$ forces $g^{-1} g' \in H$. The quotient map $G \to G/H$ has local continuous sections, since $G$ is an $l$-group and $H$ is closed. With these sections the inverse map is continuous, so the bijection is a homeomorphism.

*Step 2: the averaging map.* For $\Phi \in S(G \times F)$ define
$$A\Phi(g z) = \int_H \Phi(g h, h^{-1} z)\, d\mu_H(h).$$
The right side does not change when $(g, z)$ is replaced by $(g h', h'^{-1} z)$, by the invariance of $\mu_H$. So $A\Phi$ is a well defined function on $X$, and it lies in $S(X)$ by step 1. The map $A : S(G \times F) \to S(X)$ is surjective. To see this, cover a compact open set of $X$ by finitely many sets $U_i z$ with $U_i$ compact open in $G$ and small enough that the local sections exist on $U_i H / H$. On each piece take $\Phi = \alpha_i \otimes \varphi_i$ with $\alpha_i$ a suitable multiple of the indicator of $U_i$. The map $A$ intertwines the action of $G$ on the first factor of $G \times F$ with the action on $X$.

*Step 3: the correspondence.* Let $\xi$ be $\chi$-equivariant on $X$. Then $\xi \circ A$ is a distribution on $G \times F$ that is $\chi$-equivariant for the left translations of the first factor. Fix $\varphi \in S(F)$. The functional $\alpha \mapsto \xi(A(\alpha \otimes \varphi))$ on $S(G)$ is $\chi$-equivariant under left translation. By the uniqueness of Haar measure, it is a multiple of $\alpha \mapsto \int_G \alpha \chi\, d\mu_G$. Call the multiple $\eta(\varphi)$. Then $\eta$ is linear in $\varphi$, and $\xi(A(\alpha \otimes \varphi)) = (\int \alpha \chi)\, \eta(\varphi)$. A change of variables in $H$, together with the unimodularity of $G$ and $H$, shows that $\eta$ is $\chi|_H$-equivariant. Put $\mathrm{Fr}(\xi) = \eta$.

Conversely, let $\eta \in \mathcal{D}(F)^{H,\chi}$. The functional $\Phi \mapsto ((\chi \mu_G) \otimes \eta)(\Phi)$ on $S(G \times F)$ kills the kernel of $A$. The kernel is spanned by the differences $\Phi - \Phi^{h}$ with $\Phi^{h}(g, z) = \Phi(g h^{-1}, h z)$, and the equivariance of $\eta$ together with the unimodularity of $G$ gives the same value on $\Phi$ and $\Phi^h$. So the functional descends to a distribution $\xi$ on $X$, and $\xi$ is $\chi$-equivariant because $A$ is $G$-equivariant. The two constructions are inverse to each other, by the formula in 2 and the surjectivity of $A$.

*Step 4: supports.* Let $C$ be closed and $G$-stable. Then $g z \notin C$ if and only if $z \notin C$, for $z \in F$. So $A$ maps the functions supported in $G \times (F \setminus C)$ onto the functions supported in $X \setminus C$. Property 1 follows from the formula of step 3. $\square$

**Remark 7.1.2.** The theorem reduces a question about $G$-equivariant distributions on $X$ to a question about $H$-equivariant distributions on one fibre. In the next sections $H$ is the centralizer of a semisimple element and the fibre is a slice through it. A distribution that vanishes near the slice then vanishes near the whole orbit.

**Remark 7.1.3 (Formalization).** The statement is in [SupportedInIffOfFrob.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/BernsteinUnitaryProducts/BernsteinTheoremA/FrobeniusReciprocity/SupportedInIffOfFrob.lean#L10), and the proof in [FrobProof.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/FrobeniusReciprocity/FrobProof.lean#L301). The spaces, supports and translations are defined in [PullHomeoApply.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/BernsteinUnitaryProducts/BernsteinTheoremA/FrobeniusReciprocity/PullHomeoApply.lean). Distributions are linear maps on the space of test functions, as above. The theorem gives the isomorphism together with properties 1 and 2. It does not give a closed formula for the inverse map. The folder with the same name as this theorem also holds the induction that proves the vanishing theorem in characteristic zero, which does not use the theorem directly.
