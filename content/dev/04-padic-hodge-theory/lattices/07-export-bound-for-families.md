---
title: The export bound for families
decls:
  - Formalism.MainNotions.TwistedPlaces.stmtU_holds
  - Formalism.MainNotions.TwistedPlaces.stmtF_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The export bound for families

The local bounds of the earlier sections are used, at each prime, to bound a weighted sum over the twisted places of a global datum. This section proves that this bound holds uniformly along a family of global data indexed by a scale $x \to \infty$: if the admitted inputs hold with a constant $C_a$ for all large $x$, then the bound holds with the constant $2000 (|C_a| + 1)^3$ for all large $x$. The constant depends only on $C_a$, not on the family. The bound for one datum is [the export bound](/entry/export-bound-of-admissible/), and the result for families is used in [the main link for families](/entry/link-fam-main/).

**Definition 8.7.1 (Scale and size datum).** A *scale* is a pair of real numbers $x > 1$ and $\varepsilon$ with $0 < \varepsilon < 1/52$, together with a real number $J \ge 1$. It gives the sizes
$$\mathcal{L} = x^{\varepsilon}, \qquad b = \exp(\mathcal{L}) = \exp(x^{\varepsilon}).$$
Let $D$ be a global datum. Among its data are a number field $E$ with its places, integers $f, m, t \ge 0$, a character $\mu_0$ and a character $\mu_w$ at each place $w$, and for each $j$ and each character $\mu$ a complex vector space $Z_j(\mu)$. A *size datum* $\mathcal{S}$ for $D$ consists of a scale and further data; among them a finite set $\mathrm{supp}$ of places of $E$ and a number $N_c \ge 0$ that depends on $x$, $\varepsilon$ and $D$. A place $w$ is *twisted* if $\mu_w \ne \mu_0$. The *lifts* of $D$ are $j = 1, \dots, m$, and $d_0(j) = \dim_{\mathbb{C}} Z_j(\mu_0)$.

For a place $w$ put $\lambda(w) = \log \mathrm{N}(w) / [E' : \mathbb{Q}]$, the logarithm of the absolute norm divided by the degree of the field $E'$ of $w$, let $e(w)$ be its ramification index, and let $\eta_j(w) \in \mathbb{N}$ be a number that $D$ attaches to $j$ and $w$. The *twisted sum* of the lift $j$ is
$$\Sigma_j(\mathcal{S}) = \sum_{\substack{w \in \mathrm{supp} \\ w \text{ twisted}}} \lambda(w)\, e(w)\, \eta_j(w).$$

**Definition 8.7.2 (The export bound).** The datum $D$ gives rational numbers $\ell_l(e)$ for $l, e \in \mathbb{N}$, and its local data give, at each prime $p$ and in each degree $e$, a Tate-Shafarevich length $\ell'_p(e) \in \mathbb{N} \cup \{\infty\}$. For a prime $l$ let $v(l) = \log l \sum_{e=1}^{t-1} \ell_l(e)$, and put $v(l) = 0$ if $l$ is not a prime. Let $C \in \mathbb{R}$. The size datum $\mathcal{S}$ satisfies the *export bound with constant* $C$ if the following holds. Assume that $\ell'_p(e)$ is finite for every prime $p$ and $0 < e < t$, and that $\sum_l v(l)$ converges. Then for every lift $j$,
$$\begin{aligned} \Sigma_j(\mathcal{S}) \le d_0(j) \Bigl( &C \bigl( f m\, b\, \mathcal{L}^2 + (\log x)^2 N_c \bigr) \\ &+ \sum_{l} v(l) \Bigr). \end{aligned}$$

So the twisted sum is at most $d_0(j)$ times a fixed multiple of $b \mathcal{L}^2 = e^{x^{\varepsilon}} x^{2 \varepsilon}$, up to the term $(\log x)^2 N_c$ and the Tate-Shafarevich terms.

**Definition 8.7.3 (Admitted inputs).** Let $\mathcal{S}$ be a size datum for $D$ with a choice $P$ of parameters, and let $C \in \mathbb{R}$. The *admitted inputs with constant* $C$ hold for $(\mathcal{S}, P)$ if, when $\ell'_p(e)$ is finite for every prime $p$ and $0 < e < t$, there is a table of local lengths for $\mathcal{S}$ that satisfies seventeen conditions. The local bounds of the earlier sections enter through these conditions. The last condition says that the parameters are polynomially bounded: two constants of $P$ are at most $C$, the integers $k, n, t$ of $D$ are at most $x^C$, $x^{-\varepsilon}$ is at most a number $\delta_2$ of $\mathcal{S}$, the logarithm of a positive integer $h_E$ of $D$ is at most $C x^C$, and the logarithm of the order of a finite group attached to $D$ is at most $C x^C \mathcal{L}$.

**Definition 8.7.4 (Large scale).** A scale $(x, \varepsilon)$ is *large for* $C$ if
$$\begin{aligned} &100 \le x, \quad 10^8 (C + 1)^3 \le x, \quad 48 C \le x^{1/2}, \quad 4 \le e^{x^{\varepsilon}}, \quad 8 x \le e^{x^{\varepsilon/3}}, \\ &x^{C+2} e^{x^{\varepsilon/3}} \le e^{x^{\varepsilon}}, \quad (C+3)^2 (1 + \log x)^2 \le x^{\varepsilon}, \\ &x^{20 C + 40} e^{20 x^{\varepsilon/4}} \le e^{x^{\varepsilon/3}}. \end{aligned}$$
For fixed $\varepsilon > 0$ and $C$, every $x$ beyond some $x_0$ is large for $C$, since $\log x$ and every power of $x$ are small against $e^{x^{\delta}}$ for $\delta > 0$.

**Theorem 8.7.5 (Export bound for one datum).** Let $\mathcal{S}$ be a size datum for $D$ with parameters $P$, and $C \in \mathbb{R}$. If the scale of $\mathcal{S}$ is large for $C$ and the admitted inputs with constant $C$ hold for $(\mathcal{S}, P)$, then $\mathcal{S}$ satisfies the export bound with constant $2000 (|C| + 1)^3$.

Lean: `Formalism.MainNotions.TwistedPlaces.export_bound_of_admissible`.

*Proof.* This is [the export bound](/entry/export-bound-of-admissible/), proved in the second part of the chapter. We give its outline. One of the admitted inputs bounds a constant of $P$ that is positive by definition by $C$, so $C > 0$ and $|C| = C$. A lemma of the second part groups the twisted places by their residue characteristic $l$ and gives $\Sigma_j \le d_0(j) \bigl( 6 + \nu + \log h_E + \log |G| + \sum_{l \in S} \log l \cdot \lambda_G(l) \bigr) + d_0(j) \sum_l v(l)$, with $S$ the set of residue characteristics of the twisted places in $\mathrm{supp}$, $\nu$ a number of $D$, $|G|$ the order of the finite group above, and $\lambda_G(l)$ a local length at $l$. A second lemma bounds the bracket, with the local bounds at each $l \in S$, by $2000 (C+1)^3 f m\, b\, \mathcal{L}^2$, which is at most $2000 (C+1)^3 (f m\, b\, \mathcal{L}^2 + (\log x)^2 N_c)$ since $N_c \ge 0$. $\square$

**Definition 8.7.6 (Family).** Let $\varepsilon \in \mathbb{R}$. A *family with exponent* $\varepsilon$ consists of a threshold $x_1 > 1$, for each $x \in \mathbb{R}$ a set of indices $I_x$ with $I_0$ not empty, and for each $x$ and $i \in I_x$ a global datum $D_{x,i}$ and a size datum $\mathcal{S}_{x,i}$ for it, such that the scale of $\mathcal{S}_{x,i}$ has exponent $\varepsilon$ for all $x$, and $x$ itself when $x > x_1$. For $x > x_1$ it gives parameters $P_{x,i}$ for $\mathcal{S}_{x,i}$, and many further data and conditions, with the same constants for all $x$ and $i$.

The family satisfies the *admitted inputs with constant* $C_a$ if there is $x_0$ such that the admitted inputs with constant $C_a$ hold for $(\mathcal{S}_{x,i}, P_{x,i})$ for all $x \ge x_0$ with $x > x_1$ and all $i \in I_x$. It satisfies the *export bound with constant* $C$ if there is $x_0$ such that $\mathcal{S}_{x,i}$ satisfies the export bound with constant $C$ for all $x \ge x_0$ and all $i \in I_x$.

**Theorem 8.7.7 (Uniform export bound for families).** Let $\varepsilon \in \mathbb{R}$ and $C_a \in \mathbb{R}$. Put $C = 2000 (|C_a| + 1)^3$. Then every family with exponent $\varepsilon$ that satisfies the admitted inputs with constant $C_a$ satisfies the export bound with constant $C$.

Lean: `Formalism.MainNotions.TwistedPlaces.stmtU_holds`.

*Proof.* Let $x_0$ be the threshold of the admitted inputs. Since $I_0$ is not empty, there is a size datum $\mathcal{S}_{0,i}$; its scale has exponent $\varepsilon$, and the exponent of a scale is positive, so $\varepsilon > 0$. Hence there is $x_L$ such that every $x \ge x_L$ gives a scale $(x, \varepsilon)$ that is large for $C_a$. Let $x \ge \max(x_0, x_1 + 1, x_L)$ and $i \in I_x$. Then $x > x_1$, so the scale of $\mathcal{S}_{x,i}$ is $(x, \varepsilon)$, which is large for $C_a$, and the admitted inputs with constant $C_a$ hold for $(\mathcal{S}_{x,i}, P_{x,i})$. By [the export bound for one datum](/entry/export-bound-of-admissible/), $\mathcal{S}_{x,i}$ satisfies the export bound with constant $2000 (|C_a| + 1)^3 = C$. $\square$

**Corollary 8.7.8 (Export bound for a family).** Let $\varepsilon \in \mathbb{R}$, and let a family with exponent $\varepsilon$ satisfy the admitted inputs with some constant. Then it satisfies the export bound with some constant.

Lean: `Formalism.MainNotions.TwistedPlaces.stmtF_holds` (also `Formalism.MainNotions.TwistedPlaces.stmtF_of_stmtU`, the passage from the uniform form).

*Proof.* Let $C_a$ be the constant of the admitted inputs. By [the uniform export bound](/entry/stmt-u-holds/), the family satisfies the export bound with constant $2000 (|C_a| + 1)^3$. $\square$

**Remark 8.7.9 (Formalization).** The export bound with constant $C$ is `aux₃ L C` and the admitted inputs are `admitted L P C`, both in [TwistedPlaces.lean](lean:Development/AutomorphicArithmetic/ResidueCharacters/TwistedPlaces.lean#L123); the large scale is the structure `Large` (NEqRZeroMulXPow.lean line 418), and families are `FamP` (ParConsts.lean line 31). For a family, the export bound with a fixed constant is called `FamilyThinScalesBound` and with some constant `OrbitValuationBound`; the corollary is `KudlaFamilyStatement`, the uniform form `UniformExportStatement` (ExportFamilies.lean lines 10 to 21). These names do not describe the statements. All of them are copied as `abbrev`s into a second namespace, `Formalism.MainNotions.ExportFamilies` (ExportFamilies.lean line 31 on). In `stmtU_holds` the positivity of $\varepsilon$ is read off the index set at $x = 0$ (ExportBoundOfAdmissible.lean lines 1144 to 1147), which is why a family must have $I_0$ not empty. The threshold is $\max(x_0, \max(x_1 + 1, x_L))$. We did not unfold the seventeen conditions of the admitted inputs (`AdmT`), the exponents $\eta_j(w)$ (`etaJ`), the number $N_c$ (`budgetNc`), nor the further data of a family. The numbers $\ell_l(e)$ are a free field `shaLen` of the datum (DataRows.lean line 166), and the lengths $\ell'_p(e)$ are `Formalism.GaloisCohomology.shaLen`; we did not check that the two agree. Both the export bound and the admitted inputs assume that the lengths $\ell'_p(e)$ are finite.
