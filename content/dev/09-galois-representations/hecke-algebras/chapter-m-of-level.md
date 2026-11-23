---
id: chapter-m-of-level
title: The ordinary eigenfunctional and the Eisenstein measure at a fixed level
kind: theorem
decl: GlobalTheory.EisM.chapterM_of_level
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExists
covers: 534
status: drafted
drafted_by: writer@claude
---
This theorem is [the eigenfunctional theorem](/entry/chapter-m-holds/) at a level $N$ that is fixed in advance. It assembles the eigenfunctional, the measure and the smoothing integers from seven lemmas. `chapterM_holds` only chooses $N$ and calls it.

## Statement

Let $\ell$ be a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $e \ge 1$, $k = 2e+1$, and $g$ a newform of weight $k$ with $|\iota^{-1} a_\ell(g)| = 1$. Let $\psi$ be a character modulo $\ell$. Let $N \ge 1$ with $\ell \nmid N$, and let $r \ge 7$ be a prime with $r \mid N$. Let $\chi$ be a character modulo $N$ and $g'$ a sequence with $\mathrm{Prim}(k, N, \chi, g')$ and $g'_n = a_n(g)$ for $n$ prime to $N$.

$\mathrm{Prim}(k, N, \chi, g')$ says: $f = \sum g'_n q^n$ transforms with weight $k$ on $\Gamma_0(N)$ with character $\chi$, $g'$ has polynomial growth, $|f(\tau)|^2 (\operatorname{Im}\tau)^k$ is bounded, $g'_1 = 1$, $g'_n = 0$ when $n$ is not prime to $N$, and $g'$ is a $T_q$ eigenvector with eigenvalue $g'_q$ for each prime $q \nmid N$.

**Theorem.** Then there are $\theta$, $\alpha$, $v$, $\lambda$, $c_1$, $d_1$ with properties 2 to 6 of [the eigenfunctional theorem](/entry/chapter-m-holds/), and $N \ge 5$.

The measure condition $\mathrm{MeasMu}$ uses
$$Z(f)_n = \sum_{\substack{n_1 + n_2 = n \\ \ell \nmid n_1,\ \ell \nmid n_2}} \sum_{x_1 x_2 = n_1} \sum_{y_1 y_2 = n_2} x_1^{k-2}\, \hat\theta(x_1)\, w(y_1)\, f(x_1 / y_2),$$
where $\hat\theta(d) = \sum_{y < N} \theta(y) e^{2\pi i y d/N}$ and $w(B) = [B \equiv 1] - s[B \equiv -1] \pmod N$, with $s = (-1)^e\psi(-1)$.

## Proof

1. `odd_chi_and_tendsto_twisted_LSeries_ne_zero_of_prim`: since $k$ is odd, $\chi(-1) = -1$.
2. `exists_dirichletCharacter_parity_mul_ne_one_mul_inv_ne_one`, with the prime $r$: there is $\theta$ modulo $N$ with $\theta(-1) = s$, $\theta\chi \ne 1$ and $\theta\chi^{-1} \ne 1$.
3. The values of $\chi$ at $\ell$ are $\iota$-units and $|\iota^{-1}\ell| < 1$. So $X^2 - \chi^{-1}(\ell)a_\ell X + \chi^{-1}(\ell)\ell^{2e}$ has a unit trace and a constant term of norm less than 1. `unitRoot_split` gives roots $\alpha_0, \beta_0$ with $\alpha_0$ a unit.
4. `exists_heckeEigenfunctional_depletedEisenstein_ne_zero`: a functional on forms with character $\chi^{-1}$, with $T_q$ eigenvalues $\chi^{-1}(q)g'_q$ and $U_\ell$ eigenvalue $\alpha_0$, that is nonzero on a depleted Eisenstein product.
5. `eigenfunctionalAllCharacters_of_atkinLehner`, with a Bezout relation $Nx + \ell y = 1$, moves it by an Atkin-Lehner type matrix. The new functional $\lambda$ has eigenvalues $a_q(g)$ and $\alpha = \chi(\ell)\alpha_0$, and kills the other characters.
6. `muModelProduct_value_ne_zero_of_depleted` shows that $\alpha^{-1}\lambda(U_\ell Z(f))$ is nonzero for $f(x) = \psi(x)x^{-e}$.
7. `exists_muModel_measure_of_eigenfunctional` gives $\mathrm{MeasMu}$ with $v = \tfrac{2}{\varphi(N)}$ times that value.
8. `exists_smoothing_integers_coprime` gives $c_1$ and $d_1$.

The relation for $\alpha$ is a short computation from step 3. The rest is bookkeeping.

## In the Lean code

The theorem is in [OrdinaryEisensteinEigenfunctionalExists.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinaryEisensteinEigenfunctionalExists.lean#L39). $\mathrm{Prim}$, $\mathrm{MF}$ and $\mathrm{EigF}$ are in [PetIPSmulRight.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/PetIPSmulRight.lean#L84), and $Z$ (`Zm`), $w$ (`tw2`), `EigAll` and `MeasMu` are in [ChapterMu.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ChapterMu.lean#L16). The lemmas of steps 2 and 8 are called through the local names `chapterM_theta` and `chapterM_smooth`. We have not opened the proofs of the seven lemmas.

- The theorem has no hypothesis $\ell \ne 2$.
- The condition on $c_1$ is $c_1^e \ne z$ for all $z \in \mathbb{C}$ with $|z| = 1$. This is the complex absolute value, so it holds for every $c_1 > 1$. The condition on $d_1$ compares $|d_1^2|$ with $|d_1^{e+1}|$ and is automatic for $e \ge 2$.
- "Prim" here does not mean primitive: the form $g'$ is depleted at the primes dividing $N$.
