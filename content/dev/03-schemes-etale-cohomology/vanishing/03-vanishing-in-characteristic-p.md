---
title: Vanishing in characteristic p
decls:
  - GlobalTheory.CharPVanish.subsingleton_coh_of_decomp
  - GlobalTheory.CharPVanish.charp_of_lift
  - GlobalTheory.T.kodaira_vanishing_mod_p_squared
  - GlobalTheory.charp_vanishing_liftable
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Vanishing in characteristic p

This section proves Kawamata-Viehweg vanishing for a smooth projective variety over $\mathbb{F}_p$ of dimension $d < p$ that lifts to $\mathbb{Z}/p^2$ together with a divisor with simple normal crossings ([Theorem 9.3.3](/entry/charp-vanishing-liftable/)). The argument of Deligne and Illusie is a descent along the Frobenius: Serre vanishing holds for a large twist, and the decomposition property of Section 2 carries it down, one power of $p$ at a time. Section 4 deduces the same vanishing in characteristic $0$ by reduction modulo $p$.

Recall that a line bundle is [ample](/learn/positivity-resolution/#ample-nef-and-big-line-bundles) ([[ample|RRK8P6TXG2]]) if a positive power of it is very ample, and that Serre vanishing says that for $H$ ample and $\mathcal{F}$ coherent on a projective scheme, $H^b(X, \mathcal{F}(NH)) = 0$ for $b > 0$ and $N$ large ([coherent cohomology](/learn/commutative-algebra/#coherent-cohomology)). For $X$ smooth of relative dimension $d$ over a field, a *canonical bundle* $K$ is a line bundle with, on each open set of a trivializing affine cover, a free generator of $\Omega^d_X$, compatible with the transition functions; so $K \cong \Omega^d_X$. A *canonical divisor* $K_X$ is a Cartier divisor with $\mathcal{O}_X(K_X) \cong K$ ([[canonical divisor|W05VYY4HBR]]).

**Theorem 9.3.1 (Vanishing from the decomposition property).** Let $p$ be a prime and $X$ an integral scheme, smooth of relative dimension $d$ and projective over $\mathbb{F}_p$, with $d < p$ and canonical divisor $K_X$. Let $(E_c)_{c \in C}$ be a finite family of Cartier divisors and $\mathcal{A}$ an snc atlas of $(E_c)$ of dimension $d$, with a finite index set, that has the decomposition property. Let $M$ and $H$ be Cartier divisors with $\mathcal{O}_X(H)$ ample, $r > 0$ an integer and $0 \leq b_c < r$ integers with
$$rM = rK_X + \sum_c b_c E_c + H$$
as Cartier divisors. Then $H^q(X, \mathcal{O}_X(M)) = 0$ for all $q > 0$.

Lean: `GlobalTheory.CharPVanish.subsingleton_coh_of_decomp`.

In rational terms, $M = K_X + \sum_c \frac{b_c}{r} E_c + \frac1r H$: the boundary has coefficients in $[0, 1)$ and the rest is ample. This is the $\mathbb{Q}$-divisor form of [Kawamata-Viehweg vanishing](/learn/positivity-resolution/#kodaira-and-kawamata-viehweg-vanishing) in Volume 1.

*Proof.* Write $Z = \bigcup_c \operatorname{supp} E_c$ and $\Omega^a(G) = \Omega^a_Z(G)$, and use Čech cohomology on the atlas. The field $K$ of functions has characteristic $p$, and $X$ is separated, as it is projective. For $e \geq 0$ define
$$G_e = p^e (M - K_X) - \sum_c \Big\lfloor \frac{p^e b_c}{r} \Big\rfloor E_c - \sum_c E_c.$$

Step 1 (the recursion). For each $e$, $G_{e+1} = pG_e + \sum_c \rho_c E_c$ with $\rho_c = p - 1 - \big(\lfloor p^{e+1} b_c / r \rfloor - p \lfloor p^e b_c / r \rfloor\big)$. The difference in parentheses is a digit in base $p$, so $0 \leq \rho_c < p$. Also $G_0 = M - K_X - \sum_c E_c$, since $b_c < r$.

Step 2 (a large twist). For $0 \leq j < r$ put $R_j = j(M - K_X) - \sum_c \lfloor j b_c / r \rfloor E_c - \sum_c E_c$. Write $N = Qr + j$ with $0 \leq j < r$. Since $r(M - K_X) = \sum_c b_c E_c + H$ and $\lfloor (Qr + j) b_c / r \rfloor = Q b_c + \lfloor j b_c / r \rfloor$, we get
$$N(M - K_X) - \sum_c \Big\lfloor \frac{N b_c}{r} \Big\rfloor E_c - \sum_c E_c = QH + R_j.$$
By Serre vanishing on the atlas, there is $q_0$ such that $\check H^b(\Omega^a(QH + R_j)) = 0$ for all $Q \geq q_0$, all $j < r$, all $a$ and all $b > 0$. Put $e_0 = q_0 r$. Then $p^{e_0} \geq e_0$, so $Q = \lfloor p^{e_0} / r \rfloor \geq q_0$, and $G_{e_0} = QH + R_j$ for $j$ the remainder of $p^{e_0}$ modulo $r$.

Step 3 (vanishing at the top). Let $a + b > d$. If $a > d$, then $\Omega^a(G) = 0$, since the differentials have rank $d$. If $a \leq d$, then $b > 0$, and Step 2 gives $\check H^b(\Omega^a(G_{e_0})) = 0$. So $\check H^b(\Omega^a(G_{e_0})) = 0$ for all $a + b > d$.

Step 4 (descent). Assume $\check H^b(\Omega^a(G_{e+1})) = 0$ for all $a + b > d$. Filter the Čech-de Rham complex of $\Omega^\bullet(G_{e+1})$ by the degree of forms. The graded pieces in total degree $n > d$ have zero cohomology, so $\mathbb{H}^n(\Omega^\bullet(G_{e+1})) = 0$ for $n > d$. By Step 1, $G_{e+1} = pG_e + \sum_c \rho_c E_c$ with $\rho_c < p$, so the decomposition property gives $\check H^b(\Omega^a(G_e)) = 0$ for all $a + b > d$. A descending induction from $e_0$ gives the vanishing for $G_0$.

Step 5 (top forms). The top forms are free of rank one: there is a nonzero $\omega_0$ such that $\Omega^d(G)$ at $y$ is $\omega_0$ times the stalk of $\mathcal{O}_X(K_X + \sum_c E_c + G)$, for each $G$ and $y$. With $G = G_0$, $K_X + \sum_c E_c + G_0 = M$. So $\Omega^d(G_0) \cong \mathcal{O}_X(M)$, and Step 4 with $a = d$ gives $\check H^q(\mathcal{O}_X(M)) = 0$ for $q > 0$ on the atlas. The atlas is a finite cover by affine opens of a separated scheme, so its Čech cohomology is the cohomology of $\mathcal{O}_X(M)$. $\square$

The next theorem states the same vanishing for line bundles, with the boundary given on the lift.

**Theorem 9.3.2 (Kawamata-Viehweg vanishing for a lift modulo $p^2$, integral case).** Let $p$ be a prime, $Y$ a scheme over $\mathbb{Z}/p^2$ and $X = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$, with $\pi : X \to Y$. Assume that $X$ is integral, smooth of relative dimension $d$ and projective over $\mathbb{F}_p$, with $d < p$. Let $(L_i, \sigma_i)_{i \leq s}$ be a relative snc family of dimension $d$ on $Y$ over $\mathbb{Z}/p^2$. Let $K$ be a canonical bundle of $X$, $M$ a line bundle, $A$ an ample line bundle, $r > 0$ and $0 \leq b_i < r$ integers, with
$$r[M] = r[K] + \sum_i b_i\, \pi^*[L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$
Then $H^q(X, M) = 0$ for all $q > 0$.

Lean: `GlobalTheory.CharPVanish.charp_of_lift` (also `GlobalTheory.T.kodaira_vanishing_mod_p_squared`, a second name).

*Proof.* [Theorem 9.2.5](/entry/exists-atlas-decomp/) gives Cartier divisors $E_i$ with $\mathcal{O}_X(E_i) \cong \pi^* L_i$ and an snc atlas of $(E_i)$ of dimension $d$ with the decomposition property, on a finite index set. Each line bundle on the integral scheme $X$ is $\mathcal{O}_X(M')$ for a Cartier divisor $M'$; take one for $M$. The canonical divisor $K_X$ has class $[K]$. Put $H = rM' - rK_X - \sum_i b_i E_i$. Its class is $r[M] - r[K] - \sum_i b_i \pi^*[L_i] = [A]$, so $\mathcal{O}_X(H) \cong A$ is ample. Now $rM' = rK_X + \sum_i b_i E_i + H$ as divisors, and [Theorem 9.3.1](/entry/subsingleton-coh-of-decomp/) gives $H^q(X, \mathcal{O}_X(M')) = 0$ for $q > 0$. Since $M \cong \mathcal{O}_X(M')$, the theorem follows. $\square$

With $r = 1$ and all $b_i = 0$ the conclusion is $H^q(X, K \otimes A) = 0$: Kodaira vanishing for a variety that lifts to $\mathbb{Z}/p^2$, as Deligne and Illusie prove it (Invent. Math. 89, 1987).

**Theorem 9.3.3 (Kawamata-Viehweg vanishing for a lift modulo $p^2$).** The last theorem holds without the hypothesis that $X$ is integral.

Lean: `GlobalTheory.charp_vanishing_liftable`.

*Proof.* $X$ is smooth and quasi-compact over a field, so it is a finite disjoint union of open and closed integral subschemes $X_1, \dots, X_k$. Then $H^q(X, M) = \prod_c H^q(X_c, M|_{X_c})$, so it suffices to treat each $X_c$. As $p$ is nilpotent in $\mathbb{Z}/p^2$, $X$ and $Y$ have the same underlying space, so $X_c = W_c \times_{\mathbb{Z}/p^2} \mathbb{F}_p$ for an open subscheme $W_c$ of $Y$. The restrictions of $(L_i, \sigma_i)$ to $W_c$ form a relative snc family of dimension $d$. $X_c$ is smooth of relative dimension $d$ and projective over $\mathbb{F}_p$, as an open and closed subscheme of $X$. The restriction of $A$ to $X_c$ is ample, because $X_c \to X$ is a closed immersion. The restriction of $K$ is a canonical bundle of $X_c$, and the relation in $\operatorname{Pic}$ restricts to $X_c$. The integral case gives $H^q(X_c, M|_{X_c}) = 0$ for $q > 0$. $\square$

**Remark 9.3.4 (Formalization).** In the first theorem the relation is an equality of Cartier divisors, and `canonical f d` is a fixed canonical divisor. The inputs of its proof are the lemmas `GlobalTheory.T.serre_vanishing_snc_atlas` (Step 2), `GlobalTheory.T.cech_vanishing_frobenius_descent` (Step 4), `GlobalTheory.T.top_log_forms_canonical_generator` and `GlobalTheory.T.cech_lattice_cohomology_vanish` (Step 5), and `twist_split` in [SubsingletonCohOfDecomp.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SubsingletonCohOfDecomp.lean#L64) (Step 2). We read the statements of the first four; the filtration argument in Step 4 is our account of the descent lemma. The second name `GlobalTheory.T.kodaira_vanishing_mod_p_squared` says "Kodaira vanishing", but its statement has the fractional boundary of Kawamata-Viehweg vanishing; it is proved by `first | exact @… | …`. The vanishing is stated as `Subsingleton (coh … q)`.
