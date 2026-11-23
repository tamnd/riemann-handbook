---
title: Adelic data and joint sites
decls:
  - GlobalTheory.TwV.adLawAt_xiAd
  - GlobalTheory.T.adelicChainDatum_characterLaws_jointKernel
  - GlobalTheory.TwV.exists_adLawAt_joint
  - GlobalTheory.T.exists_adelicDatum_with_laws_at_joint
  - GlobalTheory.TwV.joint_at_nonempty
  - GlobalTheory.T.jointData_at_p_and_adelicDatum_nonempty
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Adelic data and joint sites

A joint of Section 1 is global: it lives on the finite adeles of the CM field $E$. To compare it with a formal group system at a prime $p$ we need local data at $p$: an embedding into $\mathbb{C}_p$, a formal group with a Lubin-Tate isomorphism, and a family of adelic series with its laws. This section constructs these data. A joint together with them is a *joint site*. The main result is that every joint has a site, if a curve with the right reduction exists at $p$. Sections 3 and 4 prove the laws of a site, and Section 5 uses a site to show that the system at $p$ is admitted.

### Adelic data and their laws

We keep the setting of Section 1: a datum $D$, extra data $\mathrm{ex}$, a tied kernel entry $t$, a word $u$ and a tuple $\mu$. The steps $0, 1, \dots, m$ of the chain fall into three kinds. There are matrix steps $i < m_2$, the first coupled step $i = m_2$, and the top step $i = m_2 + 1$, and $m = m_2 + 2$.

Chain charts $S_t$ for $(u, \mu)$ give at each step $i$ a finite set of chart classes. A chart class $\beta$ has a level, which consists of a lattice $\Lambda_\beta$, a compact open subgroup $U_\beta$ of the unitary group $U_i(\mathbb{A}_f)$ of the Gram form at step $i$, and a character $\chi_\beta$ of $U_\beta$. Each class $c$ of the twisted chain at step $i$ has a chart class $\beta(c)$ and a point $y_c \in U_i(\mathbb{A}_f)$. An adelic datum $A$ on $S_t$ fixes coordinates at each step, so that a homomorphism $z : E^{N(i)} \to E^{N(i+1)}$ has a form $z^{\mathrm{st}}$ in standard coordinates. It also fixes a lattice $\Lambda(x) = \mathrm{latK}(a, x, \Lambda_\beta)$ for each point $x$, and the points of the charts over $(\beta, x)$.

**Definition 5.2.1 (Adelic series family).** An *adelic series family* $\Xi$ on $S_t$ attaches a function
$$\Xi_i(\beta, \beta', x, x') : \mathrm{Hom}_E(E^{N(i)}, E^{N(i+1)}) \to K_t$$
to each step $i < m$, chart classes $\beta$ at step $i$ and $\beta'$ at step $i + 1$, and points $x \in U_i(\mathbb{A}_f)$ and $x' \in U_{i+1}(\mathbb{A}_f)$. Here $K_t$ is the field of the entry $t$.

Let $\mathrm{dt}_U : U^1(\mathbb{A}_f) \to D_t$ be a homomorphism to the determinant group of $D$, and let $a \in \mathcal{O}_E$. Let $\mu_T(j, \cdot)$ be a family of complex functions on the finite ideles of $E$.

**Definition 5.2.2 (Laws of an adelic datum).** The pair $(\Xi, \mu_T)$ *satisfies the laws* for $(A, \mathrm{dt}_U, a)$ if the following hold for all $i < m$ and all arguments.
1. Reading. At class points, $\Xi_i(\beta(c), \beta(c'), y_c, y_{c'})(z) = \Xi^{t}_i(c, c')(s(z^{\mathrm{st}}))$, where $\Xi^t$ is the family of the record of $t$ and $s$ is the seam map of $t$.
2. Rationality. If $x_1 = \gamma x$ and $x_1' = \gamma' x'$ with $\gamma, \gamma'$ in the rational unitary groups, then $\Xi_i(\beta, \beta', x_1, x_1')(z) = \Xi_i(\beta, \beta', x, x')(z_{\gamma, \gamma'})$, where $z_{\gamma, \gamma'}$ is $z$ transformed by $\gamma$ and $\gamma'$ in standard coordinates.
3. Level equivariance. If $x_1 = x \kappa$ and $x_1' = x' \kappa'$ with $\kappa \in U_\beta$ and $\kappa' \in U_{\beta'}$, then
$$\mu_T(i+1, \det \kappa')\, \chi_\beta(\kappa)\, \Xi_i(x_1, x_1')(z) = \mu_T(i+1, \det \kappa)\, \chi_{\beta'}(\kappa')\, \Xi_i(x, x')(z).$$
4. Bad places. $\Xi_i(\beta, \beta', x, x')$ depends only on the components of $x$ and $x'$ at the places of $F$ under the bad set $S$ of the record.
5. Locality and support. $\Xi_i(\beta, \beta', x, x')$ is local for the pair $(\Lambda(x), \Lambda(x'))$, and it vanishes outside the lattice of homomorphisms $\Lambda(x) \to \Lambda(x')$ divided by the level $\ell$ of the record.
6. Integrality. Every value of $\Xi$ is integral away from $S$.
7. Characters. For $y \in U^1(\mathbb{A}_f)$ we have $\mu_T(i+1, \det y) = \mathrm{mt}_{i+1}(\mathrm{dt}_U(y))$. For a class point we have $\mu_T(i+1, \det y_c) = \mathrm{mt}_{i+1}(\mathrm{dt}(c))$. The function $\mu_T(i+1, \cdot)$ is multiplicative on norm-one ideles, sends $1$ to $1$, and has algebraic values. It is $1$ on integral norm-one ideles that are trivial at the places under the tuple. Finally there are integers $e(\tau)$, equal to the infinity type of the record at step $i$, with $\mu_T(i+1, z) = \prod_\tau \tau(z)^{e(\tau)}$ for every $z \in E^\times$ with $z \bar{z} = 1$.

Informally, the laws say that $\Xi$ behaves like an automorphic family of Schwartz functions on homomorphisms between lattices, with central characters given by $\mu_T$. Compare [Hecke characters](/learn/class-field-theory/#hecke-characters) for the shape of the character laws, and [adeles and ideles](/learn/number-fields/#adeles-and-ideles) for the groups.

**Definition 5.2.3 (Canonical adelic datum).** Let $A$, $\mathrm{dt}_U$ and $a$ be as above. The *canonical series family* $\Xi_A$ is defined as follows. If there is a chart point $q$ over $(\beta, x)$ and a chart point $q'$ over $(\beta', x')$, choose such points and put
$$\Xi_A(i, \beta, \beta', x, x')(z) = \sigma_0\bigl(\xi_i(q, q')(s(z^{\mathrm{st}}))\bigr).$$
Otherwise put $\Xi_A(i, \beta, \beta', x, x') = 0$. Here $\xi_i(q, q')$ is the entry series of the chain at a matrix step, the first coupled series at the step $m_2$, and the top series at the step $m_2 + 1$. The *canonical characters* are $\mu_A(j, x) = \mathrm{mt}_j(\mathrm{dt}_U(y))$ for a chosen $y \in U^1(\mathbb{A}_f)$ with $\det y = x$, and $\mu_A(j, x) = 0$ if there is no such $y$.

**Theorem 5.2.4 (Laws of the canonical datum).** Let $A$ be an adelic datum on chain charts for $(t, u, \mu)$, and let $\mathrm{dt}_U$ and $a$ be such that $(A, \mathrm{dt}_U, a)$ has pins and a tie. Then $(\Xi_A, \mu_A)$ satisfies the laws for $(A, \mathrm{dt}_U, a)$.

Lean: `GlobalTheory.TwV.adLawAt_xiAd` (also `GlobalTheory.T.adelicChainDatum_characterLaws_jointKernel`)

*Proof.* We first collect facts from the pins and the tie.
1. Chart points exist over every pair $(\beta, x)$, and the class point $y_c$ carries the chart point $A.\mathrm{pt}(c)$.
2. The coupling coset of a class at the top equals the coset of its chart point.
3. The character laws hold for $\mu_A$ at every step. These are the laws of item 7 except the second one.
4. The series $\xi_i(q, q')$ does not depend on the chart points over $x, x'$ once the components of $x, x'$ at the places under $S$ are fixed. There are three lemmas for this, one for matrix steps, one for the first coupled step, and one for the top step.

By fact 4, the choice of chart points in the definition of $\Xi_A$ does not matter. So for any chart points $q, q'$ over $(\beta, x)$ and $(\beta', x')$, $\Xi_A(i, \beta, \beta', x, x')(z) = \sigma_0(\xi_i(q, q')(s(z^{\mathrm{st}})))$.

Reading. Take $q = A.\mathrm{pt}(c)$ and $q' = A.\mathrm{pt}(c')$. At a matrix step the tie says that the entry series at these points is the series $\Xi^t_i(c, c')$ of the record. At the first coupled step and at the top step the tie gives the same statement for the coupled series, once fact 2 replaces the coupling coset by the chart coset.

Bad places. If $x_1, x_1'$ agree with $x, x'$ at the places under $S$, choose chart points over all four. By fact 4 the two values of $\xi_i$ agree.

Level equivariance follows from fact 4 and fact 3, again by one lemma for each kind of step. Rationality, locality and support, and integrality away from $S$ each follow from a lemma on the adelic datum of a kernel chain, given facts 1 and 4.

The character laws other than the second come from fact 3. For the second, let $c$ be a class at step $k$. The class point $y_c$ lies in $U_k(\mathbb{A}_f)$, so $x = \det y_c$ satisfies $x \bar{x} = 1$. The $1 \times 1$ matrix with entry $x$ is then an element $y \in U^1(\mathbb{A}_f)$ with $\det y = \det y_c$. By the first character law $\mu_A(i+1, \det y_c) = \mathrm{mt}_{i+1}(\mathrm{dt}_U(y))$. The tie says $\mathrm{dt}_U(y) = \mathrm{dt}(c)$ for every such $y$. $\square$

**Corollary 5.2.5 (Laws at a joint).** Let $J$ be a joint for $t$ with standard data at $(u, w)$. Then there are $\Xi$ and $\mu_T$ that satisfy the laws for the adelic datum, the homomorphism $\mathrm{dt}_U$ and the element $a$ of $J$.

Lean: `GlobalTheory.TwV.exists_adLawAt_joint` (also `GlobalTheory.T.exists_adelicDatum_with_laws_at_joint`)

*Proof.* This is the theorem on the laws of the canonical datum applied to the pins and the tie of $J$. $\square$

### Joint sites

The site needs a formal group at $p$ that comes from a curve. We state its existence as a hypothesis.

**Definition 5.2.6 (Curve existence hypothesis).** The *curve existence hypothesis* says the following. Let $D$ be a datum, $\mathfrak{c}$ an ideal of $\mathcal{O}_K$ that is a curve ideal, $\delta$ a twelfth root of the discriminant of the lattice of $\mathfrak{c}$, $B$ a base and $\chi$ a character of the right type. Let $p \ge 5$ be a prime that is inert in $K$ and prime to the norm of $\mathfrak{c}$. Then for every ring map $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ there is a formal group $g$ at $p$ with a Lubin-Tate isomorphism such that the *curve condition* holds. The curve condition says that $p \ge 5$, $p$ is inert in $K$, the theta condition of $g$ at $(\mathfrak{c}, \delta)$ holds, the curve has a model over the Witt vectors, the conditions on $\mathfrak{c}$, $\delta$ and $\chi$ hold, $\lambda$ is the map of $g$, and the $2$-torsion of $g$ is the $2$-torsion of $B$.

This hypothesis is a theorem of a later section: [the formal isomorphism at a prime of good reduction](/entry/exists-genus-one-formal-iso-of-unramified-good-reduction/). Its input is the existence of good models of CM curves, see [reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models) and [complex multiplication](/learn/elliptic-curves/#complex-multiplication).

**Definition 5.2.7 (Joint site).** Let $J$ be a joint for $t$ at $(u, \mu, w)$ with standard data $\mathrm{std}$, and let $p$ be the residue characteristic of $w$. The joint data define a formal group system $\mathcal{S}$ at $p$. A *joint site* for $(J, \mathrm{std})$ consists of:
1. an embedding $E_p$ of the base field of $\mathcal{S}$ into $\mathbb{C}_p$ and a ring map $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ that agree on the field $L$;
2. a formal group $g$ at $p$ with a Lubin-Tate isomorphism, such that the curve condition holds for $(D, p, \mathfrak{c}, \delta, g, B, \chi, \lambda)$;
3. the finiteness of the classes at every level of $\mathcal{S}$, and the finiteness of the stabilizers;
4. a series family $\Xi$ and characters $\mu_T$ that satisfy the laws for the adelic datum of $J$.

The *pending tuple* of the site is the pending tuple $Y$ of $\mathcal{S}$ built from these data.

**Theorem 5.2.8 (Every joint has a site).** Assume the curve existence hypothesis. Let $J$ be a joint for $t$ with standard data $\mathrm{std}$. Then $J$ has a joint site.

Lean: `GlobalTheory.TwV.joint_at_nonempty` (also `GlobalTheory.T.jointData_at_p_and_adelicDatum_nonempty`)

*Proof.* The algebraicity conditions of $J$ give an embedding $E_p$ and a ring map $\lambda$ that agree on $L$. The index condition of $w$ says that $p \ge 5$ and that $p$ is inert in $K$. The joint says that the norm of $\mathfrak{c}$ is prime to $p$. The entry $t$ gives the conditions on $\mathfrak{c}$, $\delta$ and $\chi$. So the curve existence hypothesis applies to $\lambda$. It gives $g$ with a Lubin-Tate isomorphism and the curve condition. The corollary on laws at a joint gives $\Xi$ and $\mu_T$. Two lemmas on the system $\mathcal{S}$ give the finiteness of the classes and of the stabilizers. $\square$

**Remark 5.2.9 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.adelicChainDatum_characterLaws_jointKernel`, `GlobalTheory.T.exists_adelicDatum_with_laws_at_joint` and `GlobalTheory.T.jointData_at_p_and_adelicDatum_nonempty` are second names, each proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`.
2. The canonical family `xiAd` and the canonical characters `muOf` use `Classical.choose`, and take the value `0` off their domain (UnderTie.lean:48 and UnderTie.lean:58). On the arguments where the laws are used, the chosen objects exist.
3. The laws are the structure `AdLawAt` with thirteen fields (ExistsMidLevIff.lean:584). The joint site is the structure `Joint.At` (JointCmpEmbeddingY.lean:134). Its field `Xi` is any family with the laws, not necessarily the canonical one.
4. In `GlobalTheory.TwV.exists_adLawAt_joint` the standard data and the primality of $p$ are introduced as `_ _` and not used (ExistsAdelicDatumWithLawsAtJoint.lean:13).
5. The curve existence hypothesis is `GlobalTheory.TwV.Lt.CurveEx`, and the curve condition is `CurveIn` (StatementAdmAt.lean:29).
