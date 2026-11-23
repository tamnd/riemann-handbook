---
title: The complex points of the moduli models
decls:
  - UpperTheory.Gal.W2.GUnif_holds
  - UpperTheory.Gal.W2.gUnif_of
  - UpperTheory.Gal.W2.PDicEx_holds
  - UpperTheory.Gal.W2.RDicEx_holds
  - UpperTheory.Gal.W2.UnifG_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The complex points of the moduli models

Section 07 used six facts about the tower of Kuga-Sato varieties. The sixth fact comes from the holomorphic Lefschetz formula, and to apply that formula we must know the fixed points of the Hecke correspondences over $\mathbb{C}$. This section describes the complex points of the unitary moduli models, first as abelian varieties given by lattices and periods, and then as a set of double cosets of the unitary group. Section 09 uses both descriptions to count fixed points.

From this section to Section 12 we work with the following data. Let $p$ be a prime and $F$ a CM field with complex conjugation $c \mapsto \bar c$. This field is the field of the moduli data; in Section 07 it becomes the field $E$ through an isomorphism. Let $\mathcal{O}$ be an order with involution in a central simple $F$-algebra of degree $m$, and let $\tau_1, \dots, \tau_a$ be complex embeddings of $F$. Let $V$ be a hermitian space of dimension $n$ over $F$ that is linked to the data, and let $G$ be its unitary group. We write $\mathbb{A}_f^p$ for the finite adeles away from $p$, $K_N \subset G(\mathbb{A}_f^p)$ for the principal congruence subgroup of level $N$, $G_p$ for the group of $G$ at $p$, and $K_p \subset G_p$ for the stabiliser of the standard self-dual lattice. An infinite place $v$ of $F$ has *signature one* if the hermitian form at $v$ has exactly one positive eigenvalue.

The moduli problem of level $N$ classifies abelian varieties $A$ of dimension $g$ with an action of $\mathcal{O}$, a polarization whose Rosati involution is the involution of $\mathcal{O}$, and a full level $N$ structure. A *base* over a ring $R$ is a choice of ring maps $t_i : \mathcal{O}_F \to R$ and of an element $\rho$; over $\mathbb{C}$ it is *standard* if $t_i = \tau_i$ and $\rho$ is the fixed complex value of the data. A *generic model* of level $N$ over a field is a scheme with a universal family that represents the moduli problem there. A ring map $\rho : \mathcal{O} \to M_g(\mathbb{C})$ is *of signature type for* $t_0$ if it gives the action on the tangent space that the signature prescribes.

**Definition 3.8.1 (periods and complex uniformisation).** A *marked lattice* is a lattice $\Lambda$ with an $\mathcal{O}$-action, a perfect alternating form and a level $N$ marking. A *period* of $\Lambda$ is an additive map $P : \Lambda \to \mathbb{C}^g$ that is $\rho$-linear, whose image spans $\mathbb{C}^g$ over $\mathbb{R}$, and for which the hermitian form of the polarization is positive. A *complex uniformisation* of a family over $X$ consists of marked lattices $\Lambda_1, \dots, \Lambda_r$, one in each class of marked lattices, and maps $u_i$ from the periods of $\Lambda_i$ to $X(\mathbb{C})$ such that:

1. the fibre at $u_i(P)$ is isomorphic to $\mathbb{C}^g / P(\Lambda_i)$ with all its structure;
2. $X(\mathbb{C})$ is the disjoint union of the images of the $u_i$;
3. $u_i(P) = u_i(P')$ if and only if $P' \circ w = h \circ P$ for an automorphism $w$ of the marked lattice $\Lambda_i$ and a complex linear isomorphism $h$;
4. each $u_i$ is holomorphic in $P$, and holomorphic families of periods lift locally.

The family is *fine* if each complex point comes from a marked lattice with a period, each marked lattice with a period gives a point, and isomorphic ones give the same point.

The lattice $P(\Lambda)$ is the period lattice of the abelian variety, so a complex uniformisation is the statement that the moduli space is the space of period lattices up to isomorphism.

**Theorem 3.8.2 (complex points of the moduli model).** Suppose that $a = m = 1$ and that $\tau_1 = t_0$. Let $\rho$ be of signature type for $t_0$, let the base over $\mathbb{C}$ be standard, let $N \geq 3$ be prime to $p$, and let $X$ be a generic model of level $N$ over $\mathbb{C}$. Then $X$ is smooth of relative dimension $n - 1$, quasi-compact and separated over $\mathbb{C}$, and its universal abelian scheme is smooth of relative dimension $g$, fine, and has a complex uniformisation.

Lean: `UpperTheory.Gal.W2.GUnif_holds` (also `UpperTheory.Gal.W2.gUnif_of`).

This is the classical description of moduli of polarized abelian varieties with endomorphisms by lattices and periods (G. Shimura, On analytic families of polarized abelian varieties and automorphic functions, Ann. of Math. 78 (1963)).

*Proof.* We take as given five facts: a standard base over $\mathbb{C}$ exists; an integral model $M$ of the moduli problem exists over it ([Theorem 8.1.8 of Volume 5](/entry/model-nonempty/)); a generic model $X$ is an open and closed subscheme of the fibre of $M$; this immersion is a bijection on complex points; and fineness passes along such an immersion. By Shimura's theorem the complex points of $M$ are classified by marked lattices with periods, so the family of $M$ is fine, and by the last two facts the family of $X$ is fine. The model $M$ is smooth of relative dimension $a(n - 1) = n - 1$. An open and closed subscheme of the fibre is a base change of $M$ followed by an open immersion, so $X$ is smooth of relative dimension $n - 1$. The model $M$ is quasi-projective, so $X$ is quasi-compact, and $X$ is separated because projective space is separated. A fine family whose points are classified by marked periods has a complex uniformisation: take one marked lattice in each class and let $u_i(P)$ be the point of $\mathbb{C}^g / P(\Lambda_i)$. Clause 3 holds because the level $N$ structure is full and the $N$-th roots of unity of the base map to roots of unity in $\mathbb{C}$. $\square$

For the fixed-point count we need the points as a set of double cosets. Two dictionaries give this, one at $p$ and one at $v$. Let $\beta$ be a hermitian form in the genus of $V$ and let $\Gamma_\beta$ be its unitary group over $F$. A lattice $\Lambda \subset V$ is *perfect* for $\beta$ if $s\beta$ is perfect on $\Lambda$ for some rational $s > 0$.

**Proposition 3.8.3 (lattice dictionary at $p$).** Suppose that $a = m = 1$. For each form $\beta$ there is a map $h \mapsto \Lambda_h$ from $G_p$ to the lattices of $V$ such that each $\Lambda_h$ is perfect for $\beta$, the map is equivariant for $\Gamma_\beta$, $\Lambda_h = \Lambda_{h'}$ if and only if $h^{-1} h' \in K_p$, and each perfect lattice is some $\Lambda_h$.

Lean: `UpperTheory.Gal.W2.PDicEx_holds`.

*Proof.* Since $m = 1$ and $\beta$ is fixed by the involution, $V \otimes \mathbb{Q}_p$ has a frame: a basis in which $\beta$ has the standard form. Let $\Lambda_h$ be the lattice of $V$ whose completion at $p$ is $h$ applied to the lattice spanned by the frame, and whose completions away from $p$ are those of the standard lattice. Then $\Lambda_h$ is perfect for a power of $p$ times $\beta$, the map is equivariant, and $\Lambda_h = \Lambda_{h'}$ exactly when $h^{-1}h'$ stabilises the frame lattice, that is, when $h^{-1}h' \in K_p$. Each perfect lattice is reached because $G_p$ acts transitively on the lattices that are perfect for a multiple of $\beta$. $\square$

**Proposition 3.8.4 (period dictionary at $v$).** Suppose that $a = m = 1$ and $\tau_1 = t_0$, let $v$ have signature one, and let $\rho$ be of signature type for $t_0$. For each form $\beta$ there is a relation between periods $Q : V \to \mathbb{C}^g$ and vectors $z \in V \otimes_{v} \mathbb{C}$ such that:

1. each period $Q$ is related to some $z$ with $\beta(z, z) > 0$;
2. each $z$ with $\beta(z, z) > 0$ is related to some period $Q$;
3. if $Q$ is related to $z$ and $Q'$ to $z'$, then $Q' = h \circ Q$ for a complex linear isomorphism $h$ if and only if $z' = c z$ for some $c \in \mathbb{C}^\times$;
4. the relation is equivariant for $\Gamma_\beta$, and the eigenvalue of an element of $\Gamma_\beta$ on a fixed line $\mathbb{C} z$ matches its eigenvalue on $\mathbb{C}^g$ through the signature type.

Lean: `UpperTheory.Gal.W2.RDicEx_holds`.

So periods up to linear maps are the points of the complex ball $\mathbb{B}_\beta$ of positive lines, of dimension $n - 1$. This is the usual identification of complex structures of signature $(1, n-1)$ with the ball.

*Proof.* Choose a basis of $V \otimes_v \mathbb{C}$ that diagonalizes $\beta$, with one positive entry. For a period $Q$, the signature type splits $\mathbb{C}^g$ into the eigenspaces of $\mathcal{O}_F$. At $t_0$ the kernel of the projection of $V \otimes_v \mathbb{C}$ to its eigenspace is a hyperplane, negative definite for $\beta$, and we relate $Q$ to the vectors of its orthogonal line, which is positive. Conversely, a positive line $\mathbb{C} z$ and its orthogonal hyperplane give a complex structure on $V \otimes \mathbb{R}$ of the right signature, and so a period. At the other embeddings the form is definite and the signature type leaves no choice. Two periods differ by a linear map exactly when they give the same hyperplane, that is, the same line. Equivariance and the eigenvalue condition hold because $\Gamma_\beta$ acts on both sides through $V$. $\square$

Now put the two dictionaries together. For a form $\beta$ let $\mathcal{P}_\beta$ be the set of triples $(x, h, z)$ with $x \in G(\mathbb{A}_f^p)$, $h \in G_p$ and $z$ a vector with $\beta(z, z) > 0$, modulo $\Gamma_\beta$ acting on the left and $K_N \times K_p \times \mathbb{C}^\times$ acting on the right. Let $\mathcal{P}$ be the disjoint union of the $\mathcal{P}_\beta$ over the classes of forms in the genus.

A marked lattice $\Lambda$ with a period $P$ and an embedding $j : \Lambda \to V$ has *coordinates* $(x, h, z)$ for $\beta$ if $x$ gives the marking of $j(\Lambda)$ away from $p$, $j(\Lambda)$ is the lattice $\Lambda_h$ at $p$, and $P = Q \circ j$ for a period $Q$ related to $z$.

**Theorem 3.8.5 (group-theoretic uniformisation).** Suppose that $a = m = 1$ and $\tau_1 = t_0$, let $v$ have signature one and $\rho$ be of signature type for $t_0$, and fix a lattice dictionary and a period dictionary for each form. Let $N > 0$ be prime to $p$, and let $X$ be a family with a complex uniformisation $(u_i)$. Then there is a bijection $\Phi : X(\mathbb{C}) \to \mathcal{P}$ such that for each complex point $x$ there are a class of forms $\beta$, a triple $a$, an index $i$, a period $P$ of $\Lambda_i$ and an embedding $j$ with $\Phi(x) = [a]$ in $\mathcal{P}_\beta$, $x = u_i(P)$, and $(\Lambda_i, P, j)$ having coordinates $a$.

Lean: `UpperTheory.Gal.W2.UnifG_holds`.

This is the description of the complex points of a Shimura variety as $G(\mathbb{Q}) \backslash \mathbb{B} \times G(\mathbb{A}_f) / K$ (P. Deligne, Travaux de Shimura, Séminaire Bourbaki, exposé 389, 1971), written as a union over the classes of forms in the genus.

*Proof.* We use four facts. Each marked lattice with a period has coordinates: the lattice dictionary gives $h$, the period dictionary gives $z$, and the marking gives $x$. Each pair of a form and a triple occurs as the coordinates of some marked lattice with a period. Two marked lattices with periods are isomorphic if and only if their coordinates give the same point of $\mathcal{P}$. Coordinates move along isomorphisms of marked lattices. Define $\Phi(u_i(P))$ as the class of the coordinates of $(\Lambda_i, P)$. It is well defined by the third and fourth facts and by clause 3 of the uniformisation, injective by the third fact, and onto by the second fact and clause 2 of the uniformisation. $\square$

**Remark 3.8.6 (Formalization).** The proof of `UpperTheory.Gal.W2.gUnif_of` gets a uniformisation of $M$ from `model_uniformised`, drops it (`obtain ⟨h, hL, -⟩`), and builds the uniformisation of $X$ again with `T.complexUniformisation_of_markedPeriods_family`. The five facts of the first proof are `ModelEx`, `GenCmp`, `GenPts`, `BaseC` and `GFine`; the four facts of the last proof are `CoordEx`, `CoordOcc`, `CoordIso` and `CoordMove`. The set $\mathcal{P}$ is `GlobalTheory.LKCx.AllPts`.
