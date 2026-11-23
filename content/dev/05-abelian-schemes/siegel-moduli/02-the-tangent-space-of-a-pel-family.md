---
title: The tangent space of a PEL family
decls:
  - GlobalTheory.PelTan.finrank_derivation_le
  - GlobalTheory.T.finrank_tangent_PEL_family_le_symmetricDomain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The tangent space of a PEL family

This section introduces the unitary data of PEL type that the rest of the chapter uses, and proves the upper bound for tangent spaces: if a family of theta level objects carries a compatible action of the integers of a CM field $E$ with signature $(p, q)$, and its objects are infinitesimally rigid, then every complex tangent space of the base has dimension at most $\tfrac{[E:\mathbb{Q}]}{2}\, p q$. This is the dimension of the hermitian symmetric domain of $\mathrm{U}(p, q)$, taken once for each pair of complex conjugate embeddings of $E$. The bound is used in [the construction of PEL theta families](/entry/exists-theta-fam-is-pel-smooth/) to prove that their generic fibre is smooth of that dimension. It rests on [the injectivity of the Kodaira-Spencer map](/entry/tangent-injects-symm-antilinear/).

**Definition 5.2.1 (Host).** Let $E$ be a CM field with ring of integers $\mathcal{O}_E$ and complex conjugation $a \mapsto \bar a$. A *host* for $E$ consists of a prime $d$ with $d \equiv 7 \pmod{16}$, an element $\sqrt{-d} \in \mathcal{O}_E$ with $(\sqrt{-d})^2 = -d$, the element $w_0 \in \mathcal{O}_E$ with $2 w_0 = 1 + \sqrt{-d}$, and a complex number $\rho_0$ with $\rho_0^2 = -d$. It is also required that $\mathcal{O}_E$ is unramified over the ring of integers of the maximal real subfield $E^+$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host`.

Since $d \equiv 3 \pmod 4$, the element $w_0 = \tfrac{1 + \sqrt{-d}}{2}$ is an algebraic integer, and $\mathbb{Z}[w_0]$ is the ring of integers of $\mathbb{Q}(\sqrt{-d}) \subseteq E$. The choice of $\rho_0$ fixes which of the two square roots of $-d$ is "positive" in $\mathbb{C}$.

**Definition 5.2.2 (PEL datum).** Let $E$ carry a host. A *PEL datum* is a finite projective $\mathcal{O}_E$-module $\Lambda$ with an alternating form $\langle \cdot, \cdot \rangle : \Lambda \times \Lambda \to \mathbb{Z}$ and integers $p, q \ge 0$ such that:

1. the form is unimodular, that is $\Lambda \to \operatorname{Hom}(\Lambda, \mathbb{Z})$ is bijective;
2. $\langle a x, y \rangle = \langle x, \bar a y \rangle$ for $a \in \mathcal{O}_E$;
3. the rank of $\Lambda$ over $\mathcal{O}_E$ is $p + q$;
4. there is a complex structure $J$ on $\Lambda_\mathbb{R}$ with $J^2 = -1$ that preserves the form, with $\langle J x, x \rangle > 0$ for $x \ne 0$, such that for every $a \in \mathcal{O}_E$, $J$ commutes with $a$ and, with $t = \sum_{\tau(\sqrt{-d}) = \rho_0} \bigl(p\, \tau(a) + q\, \overline{\tau(a)}\bigr)$ (the sum over embeddings $\tau : E \to \mathbb{C}$), the trace of $a$ on $\Lambda_\mathbb{R}$ is $2 \operatorname{Re} t$ and the trace of $J a$ is $-2 \operatorname{Im} t$.

The *dimension* of the datum is $\dim D = \tfrac{[E:\mathbb{Q}]}{2}\, p q$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Datum`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Datum.dim`.

Condition 4 is the signature condition. It says that on the complex vector space $(\Lambda_\mathbb{R}, J)$ the element $a$ acts with eigenvalue $\tau(a)$ of multiplicity $p$ and $\bar\tau(a)$ of multiplicity $q$, for each embedding $\tau$ with $\tau(\sqrt{-d}) = \rho_0$. These embeddings form a CM type, one from each pair $\{\tau, \bar\tau\}$, so there are $[E:\mathbb{Q}]/2$ of them.

**Definition 5.2.3 (Semi-abelian scheme with $\mathcal{O}_E$-action).** Let $S$ be a [[scheme|5A35TYZD02]]. A *semi-abelian scheme with $\mathcal{O}_E$-action* over $S$ is a commutative semi-abelian group scheme $G \to S$ with a ring map $\mathcal{O}_E \to \operatorname{End}(G)$, $a \mapsto [a]$, a rigidified line bundle $L$ on $G$ with a cubical structure, such that $L$ is symmetric, the cubical line bundles built from $([a] \times 1)$ and $(1 \times [\bar a])$ agree for every $a$, and $L$ is isomorphic to the cubical line bundle built from $(1, [w_0])$. A *map* of such objects over $f : S' \to S$ is a cubical map $G' \to G$ that identifies $G'$ with $f^* G$ and is compatible with the actions and the cubical structures.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.SAB`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.SABMap`.

The second condition is the analogue of $\langle a x, y \rangle = \langle x, \bar a y \rangle$: the Rosati involution of $L$ restricts to complex conjugation on $\mathcal{O}_E$. Over an abelian scheme this is the usual notion of a polarized abelian scheme with $\mathcal{O}_E$-action, as in [polarizations and Zarhin's trick](/learn/abelian-varieties/#polarizations-and-zarhins-trick).

**Definition 5.2.4 (Lie multiplicity and the signature condition).** Let $G$ be as above, $k$ a field, $x : \operatorname{Spec} k \to S$ a point and $\tau : \mathcal{O}_E \to k$ a ring map. A *$\tau$-eigenvector* is a point $v \in G(k[\varepsilon])$ over $x$ that reduces to $0$ and satisfies $[a] v = \tau(a) v$ for all $a$, where $\tau(a) v$ is the image of $v$ under $\varepsilon \mapsto \tau(a)\varepsilon$. The *Lie multiplicity* of $\tau$ at $x$ is $n$ if there are $n$ eigenvectors $v_1, \dots, v_n$ such that every eigenvector is $\sum_i c_i v_i$ for a unique $c \in k^n$. Let $D$ be a PEL datum and $\rho \in k$. The action satisfies the *signature condition* at $x$ with respect to $\rho$ if every $\tau$ with $\tau(\sqrt{-d}) = \rho$ has Lie multiplicity $p$ and every other $\tau$ has Lie multiplicity $q$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.IsLieEigen`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.LieMult`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.DetCond`.

The eigenvectors are the vectors of $\operatorname{Lie}(G_x)$ on which $\mathcal{O}_E$ acts through $\tau$, so the Lie multiplicity is the dimension of the $\tau$-eigenspace of $\operatorname{Lie}(G_x)$. The signature condition is the Kottwitz determinant condition in the form of eigenspace dimensions.

**Definition 5.2.5 (Tate isomorphism).** Let $D$ be a PEL datum, $K$ a field and $G$ a semi-abelian scheme with $\mathcal{O}_E$-action over a point $x$ of $S$ with values in $K$. A *Tate isomorphism* consists of roots of unity $\zeta_n \in K^\times$, primitive of order $n$ with $\zeta_{nm}^m = \zeta_n$, and maps $\mathrm{ev}_n : \Lambda \to G(K)$ for $n \ge 1$ such that each $\mathrm{ev}_n$ is additive and $\mathcal{O}_E$-linear, has kernel $n\Lambda$ and image the $n$-torsion of $G(K)$, $m\, \mathrm{ev}_{nm} = \mathrm{ev}_n$, and the Weil pairing of $L$ satisfies $e_n(\mathrm{ev}_n a, \mathrm{ev}_n b) = \zeta_n^{\langle a, b \rangle}$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.TateIso`.

So a Tate isomorphism is an $\mathcal{O}_E$-linear symplectic isomorphism $\Lambda \otimes \widehat{\mathbb{Z}} \cong T(G_x)$, given level by level.

**Definition 5.2.6 (Symplectic basis and PEL structure).** Let $D$ be a PEL datum and $g \ge 0$. A *symplectic basis* is an isomorphism $\mathrm{bas} : \mathbb{Z}^{2g} \to \Lambda$ with $\langle \mathrm{bas}(e_i), \mathrm{bas}(e_j) \rangle = \omega(e_i, e_j)$, the standard form. Let $o$ carry a base $\zeta$ of level $k$, let $a : J \to \mathcal{O}_E$ be a map and $\rho \in o$. Let $t$ be a theta level object over $s : S \to \operatorname{Spec} o$ with endomorphisms indexed by $J$, and let $G$ be a semi-abelian scheme with $\mathcal{O}_E$-action over $S$. Then $G$ is a *PEL structure on* $t$ if there is an isomorphism of group schemes $\varphi : G \to A$ with $L_G \cong \varphi^* L$ and $\varphi \circ [a(j)] = \alpha_j \circ \varphi$ for all $j$, such that at every geometric point $x : \operatorname{Spec} K \to S$ with $K$ algebraically closed of characteristic $0$, lying over $\beta : o \to K$:

1. the signature condition holds at $x$ with respect to $\beta(\rho)$;
2. there is a Tate isomorphism with $\zeta_k = \beta(\zeta)$ and $\varphi(\mathrm{ev}_k(\mathrm{bas}(e_i))) = P_i$ for every $i$.

Lean: `GlobalTheory.ZM.IsSympBasis`, `GlobalTheory.ZM.IsPEL`, `GlobalTheory.ZM.PELClass`.

So a PEL structure says that the endomorphisms $\alpha_j$ of $t$ are the images of the elements $a(j)$ of $\mathcal{O}_E$ under an action of signature $(p, q)$, and that the level structure of $t$ is the reduction modulo $k$ of an $\mathcal{O}_E$-linear Tate isomorphism.

**Theorem 5.2.7 (Tangent bound for PEL families).** Assume the laws, the second laws, the uniformization theorem, and the theorem of the cube in the form: for every principally polarized abelian scheme $A$ and every line bundle $M$ on $A$, the line bundle $\Theta(M)$ of the cube has a generating section. Let $E$ be a CM field with a host and $D$ a PEL datum with $p + q \ge 1$. Let $g \ge 0$, let $J$ be a finite set with a map $a : J \to \mathcal{O}_E$ and elements $w, w' \in J$ with $a(w) = w_0$ and $a(w') = \bar w_0$, such that the image of $a$ generates $\mathcal{O}_E$ as a ring, and let $\mathrm{bas}$ be a symplectic basis. Let $N' \ge 1$, let $o$ carry a base of level $N'^2$, let $\rho \in o$ with $\rho^2 = -d$, and let $R$ be an $o$-algebra of finite type with a map $R \to \mathbb{C}$ compatible with a map $o \to \mathbb{C}$. Let $t$ be an infinitesimally rigid theta level object of genus $g$ and level $N'^2$ over $\operatorname{Spec} R$, with a PEL structure $G$. Then
$$\dim_\mathbb{C} \operatorname{Der}_o(R, \mathbb{C}) \le \tfrac{[E:\mathbb{Q}]}{2}\, p q.$$

Lean: `GlobalTheory.PelTan.finrank_derivation_le` (also `GlobalTheory.T.finrank_tangent_PEL_family_le_symmetricDomain`, a second name).

Here $\operatorname{Der}_o(R, \mathbb{C})$ is the complex tangent space of $\operatorname{Spec} R$ over $o$ at the given complex point, and the [[finrank|05G2G0P224]] is its dimension.

*Proof.* By [the injection theorem](/entry/tangent-injects-symm-antilinear/) there are a complex point $t_0$ of $t$, a good uniformization $u : \mathbb{C}^g \to A_0(\mathbb{C})$ with hermitian form $H$, and an injective linear map $\kappa$ from $\operatorname{Der}_o(R, \mathbb{C})$ to the matrices that are symmetric for $H$ and commute with the lift of every endomorphism of $A$ that restricts to $A_0$. So it suffices to bound the dimension of the space $V$ of such matrices.

The PEL structure gives an action of $\mathcal{O}_E$ on $A$, through $\varphi$. Its restriction to the fibre $A_0$ is an action that commutes with $m$, and by the good uniformization each $a \in \mathcal{O}_E$ lifts to a linear map $F_a$ of $\mathbb{C}^g = \operatorname{Lie}(A_0)$. The signature condition at the complex point, with $\rho_0$ the image of $\rho$ (so $\rho_0^2 = -d$), says that $\mathbb{C}^g = \bigoplus_\tau V_\tau$, where $\mathcal{O}_E$ acts on $V_\tau$ through $\tau$ and $\dim V_\tau = p$ if $\tau(\sqrt{-d}) = \rho_0$ and $q$ otherwise. A matrix $\Theta \in V$ satisfies $F_a(\Theta \bar z) = \Theta\, \overline{F_a z}$. On $z \in V_\tau$ this gives $F_a(\Theta \bar z) = \overline{\tau(a)}\, \Theta \bar z$, so the antilinear map $z \mapsto \Theta \bar z$ sends $V_\tau$ into $V_{\bar \tau}$. For each pair $\{\tau, \bar\tau\}$ with $\tau(\sqrt{-d}) = \rho_0$, $\Theta$ is given by an antilinear map $V_\tau \to V_{\bar\tau}$ and one $V_{\bar\tau} \to V_\tau$. Since $H$ is positive definite and $\langle F_a z, w \rangle_H = \langle z, F_{\bar a} w \rangle_H$, the eigenspaces are orthogonal, and the symmetry $\langle \Theta \bar z, w \rangle_H = \langle \Theta \bar w, z \rangle_H$ determines the second map from the first. The first lies in a space of real dimension $2pq$, that is of complex dimension $pq$. Summing over the $[E:\mathbb{Q}]/2$ pairs gives $\dim V \le \tfrac{[E:\mathbb{Q}]}{2} p q$, and injectivity of $\kappa$ gives the bound. $\square$

**Remark 5.2.8.** The domain of $\mathrm{U}(p, q)$, the hermitian symmetric space of type AIII, has complex dimension $pq$ (S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Chapter X). A unitary Shimura variety for $E$ of signature $(p, q)$ at each embedding of the CM type is a quotient of a product of $[E:\mathbb{Q}]/2$ such domains, which explains the number $\tfrac{[E:\mathbb{Q}]}{2} pq$. The theorem bounds the tangent spaces from above; the opposite inequality is not proved here.

**Remark 5.2.9 (Formalization).** The proof introduces seven hypotheses and never uses them: the theorem of the cube, $p + q \ge 1$, the symplectic basis condition, $a(w) = w_0$, $a(w') = \bar w_0$, the generation of $\mathcal{O}_E$ by the image of $a$, and the finite type of $R$ over $o$ ([FinrankTangentPELFamilyLeSymmetricDomain.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/FinrankTangentPELFamilyLeSymmetricDomain.lean#L22)). The statement uses one pair $(p, q)$ for all embeddings of the CM type, as the PEL datum does. The dimension $\dim D$ is written with natural division, $[E:\mathbb{Q}] / 2 \cdot p \cdot q$ ([PushInvertible.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible.lean#L24)); it is exact since $[E:\mathbb{Q}]$ is even. The PEL structure asks for the signature condition and the Tate isomorphism only at geometric points of characteristic $0$ ([ExistsArBaseAway.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/ExistsArBaseAway.lean#L22)). The cubical line bundle `cubeLB` used in the definition of the $\mathcal{O}_E$-action was not unfolded. The linear algebra step is the lemma `T.finrank_symm_antilinear_comm_CM_le`, with the eigenspace dimensions from `T.finrank_eigenspace_of_lieMultiplicity` and the action on the fibre from `FibreAct.exists_fibre_act` and `KS.exists_linear_lift_action`; we followed their statements, and the eigenspace argument above is the standard one, not a transcription of their proofs.
