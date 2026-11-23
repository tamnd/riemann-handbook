---
title: p-adic Fourier systems
decls:
  - GlobalTheory.T.thetaFourier_classSums_mem_integralClosure_galois
  - GlobalTheory.Poinc.ClassCore.classSums_integralClosure
  - GlobalTheory.T.thetaFourier_classSums_deeper_finite_extension
  - GlobalTheory.Poinc.classSums_deeper
  - GlobalTheory.T.classical_traits_fourier_terms_all_levels
  - GlobalTheory.Poinc.four_of_classical
status: drafted
drafted_by: writer@claude-opus-5-5
---
## p-adic Fourier systems

To build an ideal with prescribed orders along traits, we need functions on a rational model of a theta setup whose $p$-adic size along each classical trait is $e^{-\mathrm{sc}\,d\varphi(\beta)}$. Such functions come from Fourier expansions of theta functions: along a classical trait, a theta function is a sum of terms indexed by the period lattice, of size $e^{-\mathrm{sc}\,q_W(\beta)(\mu)}$. This section sets up the $p$-adic bookkeeping. It defines $p$-adic Fourier pre-systems, which record a family of classical traits at one point $z_1$, and proves that such a family satisfies the *Fourier condition*: sums of products of theta terms over congruence orbits are approximated by elements of the local ring at $z_1$. The proof goes through class sums in the integral closure of the local ring in a Galois extension. The result feeds the [approximation theorem](/entry/exists-approx-at/) of the next section.

Throughout, $X_1$ is a theta setup for $(F, W, i)$, with theta system $S$ of ratio $r$ and level $N_S$, rational model $Z_1$ of the field $\Omega_1$, and finite map $\pi_1 : Z_1 \to Z$. We fix a prime $p$ and $z_1 \in Z_1$, and write $A = \mathcal{O}_{Z_1, z_1}$ with maximal ideal $\mathfrak{m}_A$. For a lattice $X$, a form $\beta$ on $X$ and $\mu \in X^8$ we write $q_W(\beta)(\mu) = \sum_{u, v} W_{uv}\,\beta(\mu_u, \mu_v)$, as in the section on [Fourier term systems](/entry/exists-chart-member-traits-r/). We say $x \equiv x' \pmod N$ in a lattice $X$ if $x - x' \in NX$.

**Definition 9.16.1 ($p$-adic Fourier pre-system).** A *$p$-adic Fourier pre-system* $\Phi$ of rank at most $q$ over $A$ consists of an index set $\Phi_Y$ and, for each $y \in \Phi_Y$:

1. a ring map $\mathrm{ev}_y : A \to \bar{\mathbb{Q}}_p$ with $|\mathrm{ev}_y(h)| \le 1$ for all $h$ and $|\mathrm{ev}_y(h)| < 1$ for $h \in \mathfrak{m}_A$;
2. a free $\mathbb{Z}$-module $X_y$ of rank at most $q$;
3. a symmetric bilinear form $\beta_y$ on $X_y$ with $\beta_y(x, x) > 0$ for $x \ne 0$;
4. a real number $\mathrm{sc}_y > 0$.

Lean: `GlobalTheory.Poinc.FPre`.

The pre-system is *classical* if each index $y$ comes from a classical trait $c$ at $z_1$ for $p$: $\mathrm{ev}_y = \mathrm{val}_c$, and there is an isomorphism $e : X_y \cong Y_c$ to the lattice of the trait with $\mathrm{sc}_y\,\beta_y(a, b) = \mathrm{sc}_c\,\beta_c(e a, e b)$ for all $a, b$. Conversely $\Phi$ *matches* the classical traits if each classical trait $c$ at $z_1$ for $p$ occurs in this way for some $y$.

Lean: `GlobalTheory.Poinc.FPre.Matches`.

Only the product $\mathrm{sc}_y\,\beta_y$ is fixed by the trait, so a pre-system may rescale the form and the scale against each other. The general form of the definition has coefficients in a ring $O$ with an involution, and $\beta_y$ balanced for it; we need only $O = \mathbb{Z}$ with the identity.

**Definition 9.16.2 (Theta terms and the abelian bound).** Let $\Phi$ be a pre-system and $Q$ a set. A family $t_y(\mu, \kappa) \in \bar{\mathbb{Q}}_p$, for $y \in \Phi_Y$, $\mu \in X_y^8$ and $\kappa \in Q$, is a family of *theta terms* if
$$|t_y(\mu, \kappa)| \le e^{-\mathrm{sc}_y\,q_W(\beta_y)(\mu)}$$
for all $y, \mu, \kappa$, with equality for some $\kappa$ for each $y, \mu$. The pre-system satisfies the *abelian bound* if there is $C$ such that for each $y$ and each $x \ne 0$ in $X_y$ there is $h \in \mathfrak{m}_A$ with $e^{-C\,\mathrm{sc}_y\,\beta_y(x, x)} \le |\mathrm{ev}_y(h)|$.

Lean: `GlobalTheory.Poinc.FPre.IsTerms` (also `GlobalTheory.Poinc.FPre.abelian₂`).

The bound is the size of a Fourier coefficient of a theta function of the twisted eighth power along a trait; the theta terms are given by the next theorems, and we use only these bounds.

**Definition 9.16.3 (Unimodular maps and orbits).** Let $N, N_1 \ge 1$ and let $X_0, X$ be lattices. A $\mathbb{Z}$-linear map $k : X_0 \to X$ is *unimodular modulo $N$* if there is an isomorphism $\varepsilon : X \cong X_0$ with $\det(\varepsilon \circ k) \equiv 1 \pmod N$. For a family $a = (a_i)_{i \in I}$ in $X_0$, the *orbit* $\operatorname{orb}_{N_1, N}(k, a)$ is the set of families $\mu = (\mu_i)$ in $X$ for which there is an endomorphism $\gamma$ of $X_0$ with $\det\gamma \equiv 1 \pmod N$, $\gamma(x) \equiv x \pmod{N_1}$ for all $x$, and $\mu_i \equiv k(\gamma(a_i)) \pmod N$ for all $i$.

Lean: `GlobalTheory.Poinc.IsUnimodMod` (also `GlobalTheory.Poinc.orbit`, `GlobalTheory.Poinc.CongMod`).

For general $O$ both notions also ask that $k$ and $\gamma$ be $O$-linear modulo $N$; for $O = \mathbb{Z}$ this is automatic. So the orbit is the set of reductions modulo $N$ of the images of $a$ under the principal congruence subgroup of level $N_1$, enlarged to endomorphisms of determinant $1$ modulo $N$.

**Definition 9.16.4 (Fourier condition).** Let $N_1 \ge 1$ and $y_0 \in \Phi_Y$. Let $N \ge 1$, let $k_y : X_{y_0} \to X_y$ be linear maps, and let $t$ be theta terms. The family $(N, k, t)$ has *orbit sums* at $(N_1, y_0)$ if for each $m$, each $a \in X_{y_0}^{m \times 8}$, each $\kappa \in Q^m$ and each $e \ge 0$ there is $f \in A$ such that for each $y$ there is $h \in \mathfrak{m}_A$ with the following property: for each $\varepsilon > 0$ there is a finite set $S$ of elements of $\operatorname{orb}_{N_1, N}(k_y, a)$ such that each $\mu$ in the orbit and not in $S$ has $\exp(-\mathrm{sc}_y \sum_i q_W(\beta_y)(\mu_i)) < \varepsilon$, and
$$\Bigl|\mathrm{ev}_y(f) - \sum_{\mu \in S} \prod_{i} t_y(\mu_i, \kappa_i)\Bigr| \le \max\bigl(\varepsilon, |\mathrm{ev}_y(h)|^{e}\bigr).$$
The pre-system satisfies the *Fourier condition* at level $N_1$ if for each $y_0$ and $N_0$ there are $N \ge N_0$ with $N_1 \mid N$, maps $k_y$ with $k_{y_0} = \mathrm{id}$, each $k_y$ unimodular modulo $N$, and theta terms $t$, such that $(N, k, t)$ has orbit sums at $(N_1, y_0)$.

Lean: `GlobalTheory.Poinc.FPre.Four` (also `GlobalTheory.Poinc.FPre.OrbitSums`).

In words: the orbit sums of products of theta terms converge in $\bar{\mathbb{Q}}_p$, and one element $f$ of the local ring $A$ approximates all of them at once, uniformly in $y$, up to an error that is as small as a power $e$ of a function vanishing at $z_1$.

**Definition 9.16.5 (Class sums).** Let $B$ be an $A$-algebra and $\mathfrak{z}$ an ideal of $B$. With $N_1, N, y_0, k, t$ as above, $(N, k, t)$ has *class sums* in $(B, \mathfrak{z})$ if there are ring maps $\mathrm{ev}'_y : B \to \bar{\mathbb{Q}}_p$ that extend $\mathrm{ev}_y$, with $|\mathrm{ev}'_y| \le 1$ on $B$ and $|\mathrm{ev}'_y| < 1$ on $\mathfrak{z}$, and elements $f(c, \kappa) \in B$ for $c \in X_{y_0}^8$ and $\kappa \in Q$, such that:

1. $f(c, \kappa) = f(c', \kappa)$ whenever $c_u \equiv c'_u \pmod N$ for all $u$;
2. for each $y$, $c$, $\kappa$ and $\varepsilon > 0$ there is a finite set $S_0$ such that for each finite set $S$ of $\mu \equiv k_y(c) \pmod N$ that contains all such $\mu$ in $S_0$,
$$\Bigl|\mathrm{ev}'_y(f(c, \kappa)) - \sum_{\mu \in S} t_y(\mu, \kappa)\Bigr| \le \varepsilon;$$
3. for each automorphism $\sigma$ of $B$ over $A$ with $\sigma^{-1}(\mathfrak{z}) = \mathfrak{z}$ there is an endomorphism $\gamma$ of $X_{y_0}$ with $\det\gamma \equiv 1 \pmod N$ and $\gamma \equiv \mathrm{id} \pmod{N_1}$ (and $O$-linear modulo $N$) such that $\sigma(f(c, \kappa)) = f(\gamma c, \kappa)$ for all $c, \kappa$.

Lean: `GlobalTheory.Poinc.FPre.ClassSums`.

So $f(c, \kappa)$ is the value of the partial theta series over the congruence class of $k_y(c)$ modulo $N$, and the decomposition group of $\mathfrak{z}$ permutes these classes through congruence matrices. Clause 2 says that $\mathrm{ev}'_y(f(c, \kappa))$ is the sum of the convergent series $\sum_{\mu \equiv k_y(c)} t_y(\mu, \kappa)$.

**Theorem 9.16.6 (Class sums in an integral closure).** Let $\Phi$ be a classical $p$-adic Fourier pre-system of rank at most $g$ over $A$, let $y_0 \in \Phi_Y$ and $N_0 \ge 0$. Then there are $N \ge N_0$ with $rN_S \mid N$ and a finite Galois extension $\Omega_2$ of $\Omega_1$ with the following property. Let $B$ be the integral closure of $A$ in $\Omega_2$. For each maximal ideal $\mathfrak{z}$ of $B$ and each family of ring maps $\mathrm{ev}'_y : B \to \bar{\mathbb{Q}}_p$ that extend $\mathrm{ev}_y$, with $|\mathrm{ev}'_y| \le 1$ on $B$ and $|\mathrm{ev}'_y| < 1$ on $\mathfrak{z}$, there are maps $k_y$, a set $Q$, theta terms $t$ and elements $f(c, \kappa) \in B$ such that $k_{y_0} = \mathrm{id}$, each $k_y$ is unimodular modulo $N$, and clauses 1 to 3 of class sums hold at level $N_1 = rN_S$, without the condition of $O$-linearity in clause 3.

Lean: `GlobalTheory.Poinc.ClassCore.classSums_integralClosure` (also `GlobalTheory.T.thetaFourier_classSums_mem_integralClosure_galois`, a wrapper).

*Proof.* The sharp abelian scheme of $X_1$ has a diagonal endomorphism that is a homomorphism of monoids. With it, a theorem on deeper setups gives a theta setup $X_2$ of level $m \ge N_0$ with $rN_S \mid m$, whose field $\Omega_2$ is finite and Galois over $\Omega_1$, with a finite map $q : Z_2 \to Z_1$ of rational models; put $N = m$. A theorem on the fibre of the integral closure identifies the maximal ideals of $B$ with the points $z_2$ of $Z_2$ over $z_1$, and shows that the points of $Z_2$ over $\mathcal{O}_{\bar{\mathbb{Q}}_p}$ centred above $z_1$ at which the elements of $\mathfrak{z}$ are small are centred at $z_2$. Fix $\mathfrak{z}$ and $z_2$. A theorem on theta sums at $z_2$ gives elements $f$ of the local ring of $Z_2$ at $z_2$ and theta terms $t$ such that, along each classical trait through $z_2$ with a label, the value of $f$ is the limit of the partial theta series over a congruence class.

Each index $y$ of $\Phi$ comes from a classical trait $c_y$ at $z_1$. Lifting labels to $X_2$, a theorem on labels shows that each $c_y$ has a lift through $z_2$ and that labels are onto with known kernel; a comparison of lattices of traits with the same centre gives the maps $k_y$, which are isomorphisms with $k_{y_0} = \mathrm{id}$, unimodular modulo $N$. The theta terms of $\Phi$ are those of $c_y$ transported by $e_y$, and the identity $\mathrm{sc}_y\,q_W(\beta_y)(\mu) = \mathrm{sc}_c\,q_W(\beta_c)(e_y\mu)$ shows that they satisfy the bounds. Clause 1 holds because two elements of the local ring at $z_2$ with the same values along all lifted traits are equal, by a lemma that an element vanishing along all lifts is $0$. Clause 2 is the limit property of $f$. For clause 3, $\sigma$ restricts to an element of the Galois group of $\Omega_2$ over $\Omega_1$ that fixes $z_2$; its action on labels is given by a matrix $\gamma$ with $\gamma \equiv \mathrm{id} \pmod{rN_S}$, and $\det\gamma \equiv 1 \pmod N$ because $rN_S \ge 3$. We use only the statements of these theorems. $\square$

**Theorem 9.16.7 (Class sums in a finite extension).** Let $\Phi$ be a classical $p$-adic Fourier pre-system of rank at most $g$ over $A$, let $y_0 \in \Phi_Y$ and $N_0 \ge 0$. Then there are $N \ge N_0$ with $rN_S \mid N$, maps $k_y$, a set $Q$, theta terms $t$, a domain $B$ that is a finite $A$-algebra with finitely many automorphisms over $A$, and a maximal ideal $\mathfrak{z}$ of $B$, such that $A \to B$ is injective, the elements of $B$ fixed by all automorphisms over $A$ lie in $A$, $k_{y_0} = \mathrm{id}$, each $k_y$ is unimodular modulo $N$, and $(N, k, t)$ has class sums in $(B, \mathfrak{z})$ at $(rN_S, y_0)$.

Lean: `GlobalTheory.Poinc.classSums_deeper` (also `GlobalTheory.T.thetaFourier_classSums_deeper_finite_extension`, a wrapper).

*Proof.* Take $N$ and $\Omega_2$ from the previous theorem and let $B$ be the integral closure of $A$ in $\Omega_2$. The local ring $A$ is a noetherian normal domain whose fraction field is $\Omega_1$, as $Z_1$ is normal and of finite type over a Dedekind domain. A lemma on Galois integral closures shows that $B$ is a finite $A$-module with finitely many automorphisms over $A$, that $A \to B$ is injective, and that the elements of $B$ fixed by all these automorphisms lie in $A$. These are classical: finiteness holds for a noetherian integrally closed domain and a finite separable extension of its fraction field (M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Proposition 5.17), and an invariant element lies in $\Omega_1$ ([Galois theory](/learn/algebra/#galois-theory)) and is integral over $A$, so it lies in $A$. Choose a maximal ideal $\mathfrak{z}$ of $B$. A theorem on extensions of integral $p$-adic evaluations extends each $\mathrm{ev}_y$ to $\mathrm{ev}'_y$ on $B$ with $|\mathrm{ev}'_y| \le 1$ and $|\mathrm{ev}'_y| < 1$ on $\mathfrak{z}$. The previous theorem then gives $k$, $Q$, $t$ and $f$. The condition that $\gamma$ be $\mathbb{Z}$-linear modulo $N$ holds with difference $0$, since $\gamma$ is $\mathbb{Z}$-linear. $\square$

**Theorem 9.16.8 (Fourier condition from classical traits).** Assume that $W + W^{T}$ is positive definite. Let $\Phi$ be a classical $p$-adic Fourier pre-system of rank at most $g$ over $A$. Then $\Phi$ satisfies the Fourier condition at level $rN_S$.

Lean: `GlobalTheory.Poinc.four_of_classical` (also `GlobalTheory.T.classical_traits_fourier_terms_all_levels`, a wrapper).

*Proof.* Let $y_0 \in \Phi_Y$ and $N_0 \ge 0$. Apply the previous theorem with $N_0 + 1$; it gives $N \ge N_0 + 1 \ge 1$ with $rN_S \mid N$, and $k$, $t$, $B$, $\mathfrak{z}$ with class sums. The ring $A$ is a noetherian normal domain. A theorem on orbit traces of Galois class sums then turns the class sums in $(B, \mathfrak{z})$ into orbit sums at $(rN_S, y_0)$. Its hypotheses are that $A$ is a noetherian normal domain, that $A \to B$ is injective with invariants $A$, that $\mathfrak{z}$ is maximal, that $N \ge 1$, that $W + W^T$ is positive definite and that each $k_y$ is unimodular modulo $N$. We use only its statement. $\square$

**Remark 9.16.9 (Formalization).** In `classSums_integralClosure` the bound $|\mathrm{ev}'_y| \le 1$ is introduced but not used ([ThetaFourierClassSumsMemIntegralClosureGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaFourierClassSumsMemIntegralClosureGalois.lean#L185)). In `classSums_deeper` the congruence for $O$-linearity of $\gamma$ is proved with the witness `0`, since $O = \mathbb{Z}$ ([ThetaFourierClassSumsDeeperFiniteExtension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaFourierClassSumsDeeperFiniteExtension.lean#L28)). The hypothesis that $\Phi$ is classical is written out in each statement rather than named. The lemmas on deeper setups, fibres of integral closures, theta sums, labels, Galois actions, $p$-adic extensions and orbit traces have no entries in this part; we use only their statements.
